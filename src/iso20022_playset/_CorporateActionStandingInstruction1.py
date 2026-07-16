# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount17
from . import Max350Text
from . import SecuritiesAccount6
from . import StandingInstructionGrossNet1Code

class CorporateActionStandingInstruction1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CshDstrbtnDtls", "_NetOrGrss", "_SctiesDstrbtnDtls"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@property
	def CshDstrbtnDtls(self):
		return self._CshDstrbtnDtls

	@CshDstrbtnDtls.setter
	def CshDstrbtnDtls(self, value):
		self._CshDstrbtnDtls = value if value is not None else base_types.UninitialisedField(self, 'CshDstrbtnDtls', CashAccount17, False)

	@CshDstrbtnDtls.deleter
	def CshDstrbtnDtls(self):
		del self._CshDstrbtnDtls
		self._CshDstrbtnDtls = base_types.UninitialisedField(self, 'CshDstrbtnDtls', CashAccount17, False)

	@property
	def NetOrGrss(self):
		return self._NetOrGrss

	@NetOrGrss.setter
	def NetOrGrss(self, value):
		self._NetOrGrss = value if value is not None else base_types.UninitialisedField(self, 'NetOrGrss', StandingInstructionGrossNet1Code, False)

	@NetOrGrss.deleter
	def NetOrGrss(self):
		del self._NetOrGrss
		self._NetOrGrss = base_types.UninitialisedField(self, 'NetOrGrss', StandingInstructionGrossNet1Code, False)

	@property
	def SctiesDstrbtnDtls(self):
		return self._SctiesDstrbtnDtls

	@SctiesDstrbtnDtls.setter
	def SctiesDstrbtnDtls(self, value):
		self._SctiesDstrbtnDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesDstrbtnDtls', SecuritiesAccount6, False)

	@SctiesDstrbtnDtls.deleter
	def SctiesDstrbtnDtls(self):
		del self._SctiesDstrbtnDtls
		self._SctiesDstrbtnDtls = base_types.UninitialisedField(self, 'SctiesDstrbtnDtls', SecuritiesAccount6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshDstrbtnDtls', type=CashAccount17, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NetOrGrss', type=StandingInstructionGrossNet1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesDstrbtnDtls', type=SecuritiesAccount6, min=0, max=1, mutex_group=1, array=False),
	))