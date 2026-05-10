import base_types
import StandingInstructionGrossNet1Code
import SecuritiesAccount6
import Max350Text
import CashAccount17

class CorporateActionStandingInstruction1(base_types._BaseFieldType):

	__slots__ = ["_NetOrGrss", "_CshDstrbtnDtls", "_AddtlInf", "_SctiesDstrbtnDtls"]
	@property
	def NetOrGrss(self):
		return self._NetOrGrss

	@NetOrGrss.setter
	def NetOrGrss(self, value):
		self._NetOrGrss = value if type(value) != auto else self.make_default("NetOrGrss")

	@NetOrGrss.deleter
	def NetOrGrss(self):
		del self._NetOrGrss
		self._NetOrGrss = None

	@property
	def CshDstrbtnDtls(self):
		return self._CshDstrbtnDtls

	@CshDstrbtnDtls.setter
	def CshDstrbtnDtls(self, value):
		self._CshDstrbtnDtls = value if type(value) != auto else self.make_default("CshDstrbtnDtls")

	@CshDstrbtnDtls.deleter
	def CshDstrbtnDtls(self):
		del self._CshDstrbtnDtls
		self._CshDstrbtnDtls = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def SctiesDstrbtnDtls(self):
		return self._SctiesDstrbtnDtls

	@SctiesDstrbtnDtls.setter
	def SctiesDstrbtnDtls(self, value):
		self._SctiesDstrbtnDtls = value if type(value) != auto else self.make_default("SctiesDstrbtnDtls")

	@SctiesDstrbtnDtls.deleter
	def SctiesDstrbtnDtls(self):
		del self._SctiesDstrbtnDtls
		self._SctiesDstrbtnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetOrGrss', type=StandingInstructionGrossNet1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshDstrbtnDtls', type=CashAccount17, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesDstrbtnDtls', type=SecuritiesAccount6, min=0, max=1, mutex_group=1, array=False),
	))

