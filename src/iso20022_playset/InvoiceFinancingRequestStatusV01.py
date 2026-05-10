from . import base_types
import FinancingInformationAndStatus1
import MessageIdentification1
import OriginalRequestInformation1

class InvoiceFinancingRequestStatusV01(base_types._BaseFieldType):

	__slots__ = ["_FincgInfAndSts", "_StsId", "_OrgnlReqInfAndSts"]
	@property
	def FincgInfAndSts(self):
		return self._FincgInfAndSts

	@FincgInfAndSts.setter
	def FincgInfAndSts(self, value):
		self._FincgInfAndSts = value if type(value) != auto else self.make_default("FincgInfAndSts")

	@FincgInfAndSts.deleter
	def FincgInfAndSts(self):
		del self._FincgInfAndSts
		self._FincgInfAndSts = None

	@property
	def StsId(self):
		return self._StsId

	@StsId.setter
	def StsId(self, value):
		self._StsId = value if type(value) != auto else self.make_default("StsId")

	@StsId.deleter
	def StsId(self):
		del self._StsId
		self._StsId = None

	@property
	def OrgnlReqInfAndSts(self):
		return self._OrgnlReqInfAndSts

	@OrgnlReqInfAndSts.setter
	def OrgnlReqInfAndSts(self, value):
		self._OrgnlReqInfAndSts = value if type(value) != auto else self.make_default("OrgnlReqInfAndSts")

	@OrgnlReqInfAndSts.deleter
	def OrgnlReqInfAndSts(self):
		del self._OrgnlReqInfAndSts
		self._OrgnlReqInfAndSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FincgInfAndSts', type=FinancingInformationAndStatus1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlReqInfAndSts', type=OriginalRequestInformation1, min=1, max=1, mutex_group=None, array=False),
	))

