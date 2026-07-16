# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationRequestInformation1
from . import MessageIdentification1

class InvoiceFinancingCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_CxlReqId", "_CxlReqInf"]
	@property
	def CxlReqId(self):
		return self._CxlReqId

	@CxlReqId.setter
	def CxlReqId(self, value):
		self._CxlReqId = value if value is not None else base_types.UninitialisedField(self, 'CxlReqId', MessageIdentification1, False)

	@CxlReqId.deleter
	def CxlReqId(self):
		del self._CxlReqId
		self._CxlReqId = base_types.UninitialisedField(self, 'CxlReqId', MessageIdentification1, False)

	@property
	def CxlReqInf(self):
		return self._CxlReqInf

	@CxlReqInf.setter
	def CxlReqInf(self, value):
		self._CxlReqInf = value if value is not None else base_types.UninitialisedField(self, 'CxlReqInf', CancellationRequestInformation1, False)

	@CxlReqInf.deleter
	def CxlReqInf(self):
		del self._CxlReqInf
		self._CxlReqInf = base_types.UninitialisedField(self, 'CxlReqInf', CancellationRequestInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlReqInf', type=CancellationRequestInformation1, min=1, max=1, mutex_group=None, array=False),
	))