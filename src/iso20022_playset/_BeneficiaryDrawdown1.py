# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import BeneficiaryType1Choice
from . import YesNoIndicator

class BeneficiaryDrawdown1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_BnfcryTp", "_DthUdrLmt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def BnfcryTp(self):
		return self._BnfcryTp

	@BnfcryTp.setter
	def BnfcryTp(self, value):
		self._BnfcryTp = value if value is not None else base_types.UninitialisedField(self, 'BnfcryTp', BeneficiaryType1Choice, False)

	@BnfcryTp.deleter
	def BnfcryTp(self):
		del self._BnfcryTp
		self._BnfcryTp = base_types.UninitialisedField(self, 'BnfcryTp', BeneficiaryType1Choice, False)

	@property
	def DthUdrLmt(self):
		return self._DthUdrLmt

	@DthUdrLmt.setter
	def DthUdrLmt(self, value):
		self._DthUdrLmt = value if value is not None else base_types.UninitialisedField(self, 'DthUdrLmt', YesNoIndicator, False)

	@DthUdrLmt.deleter
	def DthUdrLmt(self):
		del self._DthUdrLmt
		self._DthUdrLmt = base_types.UninitialisedField(self, 'DthUdrLmt', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BnfcryTp', type=BeneficiaryType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DthUdrLmt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))