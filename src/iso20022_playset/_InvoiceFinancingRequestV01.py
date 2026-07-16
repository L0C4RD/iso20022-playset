# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvoiceRequestInformation1
from . import RequestGroupInformation1

class InvoiceFinancingRequestV01(base_types._BaseFieldType):

	__slots__ = ["_InvcReqInf", "_ReqGrpInf"]
	@property
	def InvcReqInf(self):
		return self._InvcReqInf

	@InvcReqInf.setter
	def InvcReqInf(self, value):
		self._InvcReqInf = value if value is not None else base_types.UninitialisedField(self, 'InvcReqInf', InvoiceRequestInformation1, True)

	@InvcReqInf.deleter
	def InvcReqInf(self):
		del self._InvcReqInf
		self._InvcReqInf = base_types.UninitialisedField(self, 'InvcReqInf', InvoiceRequestInformation1, True)

	@property
	def ReqGrpInf(self):
		return self._ReqGrpInf

	@ReqGrpInf.setter
	def ReqGrpInf(self, value):
		self._ReqGrpInf = value if value is not None else base_types.UninitialisedField(self, 'ReqGrpInf', RequestGroupInformation1, False)

	@ReqGrpInf.deleter
	def ReqGrpInf(self):
		del self._ReqGrpInf
		self._ReqGrpInf = base_types.UninitialisedField(self, 'ReqGrpInf', RequestGroupInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvcReqInf', type=InvoiceRequestInformation1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqGrpInf', type=RequestGroupInformation1, min=1, max=1, mutex_group=None, array=False),
	))