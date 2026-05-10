from . import base_types
from ._OriginalMessageAndIssuer1 import OriginalMessageAndIssuer1
from ._PaymentIdentification8Choice import PaymentIdentification8Choice
from ._RequestHandling4 import RequestHandling4

class Receipt7(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMsgId", "_OrgnlPmtId", "_ReqHdlg"]
	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if type(value) != base_types.auto else self.make_default("OrgnlMsgId")

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = None

	@property
	def OrgnlPmtId(self):
		return self._OrgnlPmtId

	@OrgnlPmtId.setter
	def OrgnlPmtId(self, value):
		self._OrgnlPmtId = value if type(value) != base_types.auto else self.make_default("OrgnlPmtId")

	@OrgnlPmtId.deleter
	def OrgnlPmtId(self):
		del self._OrgnlPmtId
		self._OrgnlPmtId = None

	@property
	def ReqHdlg(self):
		return self._ReqHdlg

	@ReqHdlg.setter
	def ReqHdlg(self, value):
		self._ReqHdlg = value if type(value) != base_types.auto else self.make_default("ReqHdlg")

	@ReqHdlg.deleter
	def ReqHdlg(self):
		del self._ReqHdlg
		self._ReqHdlg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlMsgId', type=OriginalMessageAndIssuer1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtId', type=PaymentIdentification8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqHdlg', type=RequestHandling4, min=0, max=None, mutex_group=None, array=True),
	))

