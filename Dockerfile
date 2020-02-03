FROM openapitools/openapi-generator-cli
ENV WDIR /opt/openapi-generator/modules/openapi-generator-cli/target/
WORKDIR ${WDIR}
COPY sensibo.openapi.yaml .
CMD ["java", "-jar", "openapi-generator-cli.jar"]