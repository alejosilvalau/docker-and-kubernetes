# Initial stage, using local platform
FROM --platform=$BUILDPLATFORM golang:1.21 AS build
# Copy source into place
WORKDIR /src
COPY . .

# Pull the environment variables from the host
ARG TARGETOS TARGETARCH
# Compile code using the ARG variables
RUN env GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o /final/app .

# Create container and load the cross-compiled code
FROM alpine
COPY --from=build /final/app /bin