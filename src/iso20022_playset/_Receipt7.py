# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OriginalMessageAndIssuer1
from . import PaymentIdentification8Choice
from . import RequestHandling4

class Receipt7(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMsgId", "_OrgnlPmtId", "_ReqHdlg"]
	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgId', OriginalMessageAndIssuer1, False)

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = base_types.UninitialisedField(self, 'OrgnlMsgId', OriginalMessageAndIssuer1, False)

	@property
	def OrgnlPmtId(self):
		return self._OrgnlPmtId

	@OrgnlPmtId.setter
	def OrgnlPmtId(self, value):
		self._OrgnlPmtId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPmtId', PaymentIdentification8Choice, False)

	@OrgnlPmtId.deleter
	def OrgnlPmtId(self):
		del self._OrgnlPmtId
		self._OrgnlPmtId = base_types.UninitialisedField(self, 'OrgnlPmtId', PaymentIdentification8Choice, False)

	@property
	def ReqHdlg(self):
		return self._ReqHdlg

	@ReqHdlg.setter
	def ReqHdlg(self, value):
		self._ReqHdlg = value if value is not None else base_types.UninitialisedField(self, 'ReqHdlg', RequestHandling4, True)

	@ReqHdlg.deleter
	def ReqHdlg(self):
		del self._ReqHdlg
		self._ReqHdlg = base_types.UninitialisedField(self, 'ReqHdlg', RequestHandling4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlMsgId', type=OriginalMessageAndIssuer1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtId', type=PaymentIdentification8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqHdlg', type=RequestHandling4, min=0, max=None, mutex_group=None, array=True),
	))