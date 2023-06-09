from typing import Optional

from dependency_injector import providers

# Test 1: to check the return type
provider1 = providers.Delegate(providers.Provider())
var1: providers.Provider = provider1()

# Test 2: to check the return type with await
provider2 = providers.Delegate(providers.Provider())
async def _async2() -> None:
    var1: providers.Provider = await provider2()  # type: ignore
    var2: providers.Provider = await provider2.async_()

# Test 3: to check class type from provider
provider3 = providers.Delegate(providers.Provider())
provided_provides: Optional[providers.Provider] = provider3.provides
