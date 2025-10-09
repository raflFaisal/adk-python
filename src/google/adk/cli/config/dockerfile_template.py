# config/dockerfile_template.py

_DOCKERFILE_TEMPLATE = """
FROM python:3.11-slim
WORKDIR /app

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Switch to the non-root user
USER myuser

# Set up environment variables
ENV PATH="/home/myuser/.local/bin:$PATH"

# Install ADK
RUN pip install google-adk=={adk_version}

# Copy agent
# Set permission
COPY --chown=myuser:myuser "agents/{app_name}/" "/app/agents/{app_name}/"
{install_agent_deps}

EXPOSE {port}

CMD adk {command} --port={port} {host_option} {service_option} {trace_to_cloud_option} {allow_origins_option} {a2a_option} "/app/agents"
"""
