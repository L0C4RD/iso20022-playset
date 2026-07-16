# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancingInformationAndStatus1
from . import MessageIdentification1
from . import OriginalRequestInformation1

class InvoiceFinancingRequestStatusV01(base_types._BaseFieldType):

	__slots__ = ["_FincgInfAndSts", "_OrgnlReqInfAndSts", "_StsId"]
	@property
	def FincgInfAndSts(self):
		return self._FincgInfAndSts

	@FincgInfAndSts.setter
	def FincgInfAndSts(self, value):
		self._FincgInfAndSts = value if value is not None else base_types.UninitialisedField(self, 'FincgInfAndSts', FinancingInformationAndStatus1, False)

	@FincgInfAndSts.deleter
	def FincgInfAndSts(self):
		del self._FincgInfAndSts
		self._FincgInfAndSts = base_types.UninitialisedField(self, 'FincgInfAndSts', FinancingInformationAndStatus1, False)

	@property
	def OrgnlReqInfAndSts(self):
		return self._OrgnlReqInfAndSts

	@OrgnlReqInfAndSts.setter
	def OrgnlReqInfAndSts(self, value):
		self._OrgnlReqInfAndSts = value if value is not None else base_types.UninitialisedField(self, 'OrgnlReqInfAndSts', OriginalRequestInformation1, False)

	@OrgnlReqInfAndSts.deleter
	def OrgnlReqInfAndSts(self):
		del self._OrgnlReqInfAndSts
		self._OrgnlReqInfAndSts = base_types.UninitialisedField(self, 'OrgnlReqInfAndSts', OriginalRequestInformation1, False)

	@property
	def StsId(self):
		return self._StsId

	@StsId.setter
	def StsId(self, value):
		self._StsId = value if value is not None else base_types.UninitialisedField(self, 'StsId', MessageIdentification1, False)

	@StsId.deleter
	def StsId(self):
		del self._StsId
		self._StsId = base_types.UninitialisedField(self, 'StsId', MessageIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FincgInfAndSts', type=FinancingInformationAndStatus1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlReqInfAndSts', type=OriginalRequestInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))