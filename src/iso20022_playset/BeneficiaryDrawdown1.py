from . import base_types
import AdditionalInformation15
import YesNoIndicator
import BeneficiaryType1Choice

class BeneficiaryDrawdown1(base_types._BaseFieldType):

	__slots__ = ["_BnfcryTp", "_DthUdrLmt", "_AddtlInf"]
	@property
	def BnfcryTp(self):
		return self._BnfcryTp

	@BnfcryTp.setter
	def BnfcryTp(self, value):
		self._BnfcryTp = value if type(value) != auto else self.make_default("BnfcryTp")

	@BnfcryTp.deleter
	def BnfcryTp(self):
		del self._BnfcryTp
		self._BnfcryTp = None

	@property
	def DthUdrLmt(self):
		return self._DthUdrLmt

	@DthUdrLmt.setter
	def DthUdrLmt(self, value):
		self._DthUdrLmt = value if type(value) != auto else self.make_default("DthUdrLmt")

	@DthUdrLmt.deleter
	def DthUdrLmt(self):
		del self._DthUdrLmt
		self._DthUdrLmt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfcryTp', type=BeneficiaryType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DthUdrLmt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
	))

