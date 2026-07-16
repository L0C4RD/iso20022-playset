# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DistributionPolicy1Code
from . import FormOfSecurity1Code
from . import RestrictedFINXMax35Text
from . import SecurityClassificationType3Choice

class FinancialInstrument76(base_types._BaseFieldType):

	__slots__ = ["_ClssTp", "_ClssfctnTp", "_DstrbtnPlcy", "_SctiesForm", "_SplmtryId"]
	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if value is not None else base_types.UninitialisedField(self, 'ClssTp', RestrictedFINXMax35Text, False)

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = base_types.UninitialisedField(self, 'ClssTp', RestrictedFINXMax35Text, False)

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', SecurityClassificationType3Choice, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', SecurityClassificationType3Choice, False)

	@property
	def DstrbtnPlcy(self):
		return self._DstrbtnPlcy

	@DstrbtnPlcy.setter
	def DstrbtnPlcy(self, value):
		self._DstrbtnPlcy = value if value is not None else base_types.UninitialisedField(self, 'DstrbtnPlcy', DistributionPolicy1Code, False)

	@DstrbtnPlcy.deleter
	def DstrbtnPlcy(self):
		del self._DstrbtnPlcy
		self._DstrbtnPlcy = base_types.UninitialisedField(self, 'DstrbtnPlcy', DistributionPolicy1Code, False)

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if value is not None else base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@property
	def SplmtryId(self):
		return self._SplmtryId

	@SplmtryId.setter
	def SplmtryId(self, value):
		self._SplmtryId = value if value is not None else base_types.UninitialisedField(self, 'SplmtryId', RestrictedFINXMax35Text, False)

	@SplmtryId.deleter
	def SplmtryId(self):
		del self._SplmtryId
		self._SplmtryId = base_types.UninitialisedField(self, 'SplmtryId', RestrictedFINXMax35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssTp', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=SecurityClassificationType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryId', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
	))