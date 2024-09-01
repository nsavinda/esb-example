import org.apache.camel.builder.RouteBuilder
import org.apache.camel.impl.DefaultCamelContext

class RestToKafkaRoute extends RouteBuilder {
    @Override
    void configure() throws Exception {
        // REST API configuration
        restConfiguration()
            .component("netty-http")
            .host("0.0.0.0")
            .port(8180)

        rest("/messages")
            .post()
            .to("log:received") // Log received message

        from("direct:logRequest")
            .log("Incoming request: \${headers}, Body: \${body}")
            .filter(body().isNotNull()) // Filter out null bodies
            .filter(body().regex(".+")) // Filter out empty bodies
            .log("Received Message: \${body}")
            .to("kafka:my-topic?brokers=kafka:9092")
            // .to("log:processed"); // Log after processing
    }
}


class RestToKafka {
    static void main(String[] args) {
        def context = new DefaultCamelContext()
        context.addRoutes(new RestToKafkaRoute())
        context.start()

        println("REST API is running on http://localhost:8381/messages")

        // Keep the context running
        addShutdownHook {
            context.stop()
        }

        synchronized(this) { wait() }
    }
}
