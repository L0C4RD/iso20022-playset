import base_types
import ExternalEnquiryRequestType1Code
import ExternalPaymentControlRequestType1Code
import GenericIdentification1

class RequestType4Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_PmtCtrl", "_Enqry"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def PmtCtrl(self):
		return self._PmtCtrl

	@PmtCtrl.setter
	def PmtCtrl(self, value):
		self._PmtCtrl = value if type(value) != auto else self.make_default("PmtCtrl")

	@PmtCtrl.deleter
	def PmtCtrl(self):
		del self._PmtCtrl
		self._PmtCtrl = None

	@property
	def Enqry(self):
		return self._Enqry

	@Enqry.setter
	def Enqry(self, value):
		self._Enqry = value if type(value) != auto else self.make_default("Enqry")

	@Enqry.deleter
	def Enqry(self):
		del self._Enqry
		self._Enqry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtCtrl', type=ExternalPaymentControlRequestType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Enqry', type=ExternalEnquiryRequestType1Code, min=0, max=1, mutex_group=1, array=False),
	))

