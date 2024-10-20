from infrahub_sdk.generator import InfrahubGenerator


class WidgetGenerator(InfrahubGenerator):
    async def generate(self, data: dict) -> None:
        widget = data["TestWidget"]["edges"][0]["node"]
        widget_name: str = widget["name"]["value"]
        widget_count: str = widget["count"]["value"]

        for count in range(1, widget_count + 1):

            payload = {
                "name": f"{widget_name.lower()}-{count}",
            }
            obj = await self.client.create(kind="TestResource", data=payload)
            await obj.save(allow_upsert=True)
