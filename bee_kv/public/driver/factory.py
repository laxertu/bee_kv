import bee_kv.public.driver.entities as e

import bee_kv.application.driver.implementations as i
import bee_kv.public.driver.ports as p

_handlers_map: dict[str, i.BaseHandler] = {
    p.CMD_SAVE: i.Save(),
    p.CMD_GET: i.Get(),
    p.CMD_REMOVE: i.Remove(),
    p.CMD_GET_ALL: i.GetAll(),
    p.CMD_RESET: i.Reset(),
}


def get_request(cmd: str) -> e.KvDataOperationRequest:
    return e.KvDataOperationRequest(cmd=cmd, payload=e.KvDto())


def get_handler(cmd: str) -> i.BaseHandler:
    return _handlers_map[cmd]
