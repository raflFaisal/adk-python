from abc import ABC
from abc import abstractmethod
from typing import Tuple


class Deployer(ABC):

  @abstractmethod
  def deploy(
      self,
      temp_folder: str,
      service_name: str,
      provider_args: Tuple[str],  
      env_vars: Tuple[str],
      **kwargs,
  ):
    """Deploys the agent to the target platform."""
    pass
