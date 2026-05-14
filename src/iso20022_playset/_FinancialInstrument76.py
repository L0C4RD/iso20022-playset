# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DistributionPolicy1Code import DistributionPolicy1Code
from ._FormOfSecurity1Code import FormOfSecurity1Code
from ._RestrictedFINXMax35Text import RestrictedFINXMax35Text
from ._SecurityClassificationType3Choice import SecurityClassificationType3Choice

class FinancialInstrument76(base_types._BaseFieldType):

	__slots__ = ["_ClssTp", "_ClssfctnTp", "_DstrbtnPlcy", "_SctiesForm", "_SplmtryId"]
	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if type(value) != base_types.auto else self.make_default("ClssTp")

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = None

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def DstrbtnPlcy(self):
		return self._DstrbtnPlcy

	@DstrbtnPlcy.setter
	def DstrbtnPlcy(self, value):
		self._DstrbtnPlcy = value if type(value) != base_types.auto else self.make_default("DstrbtnPlcy")

	@DstrbtnPlcy.deleter
	def DstrbtnPlcy(self):
		del self._DstrbtnPlcy
		self._DstrbtnPlcy = None

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if type(value) != base_types.auto else self.make_default("SctiesForm")

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = None

	@property
	def SplmtryId(self):
		return self._SplmtryId

	@SplmtryId.setter
	def SplmtryId(self, value):
		self._SplmtryId = value if type(value) != base_types.auto else self.make_default("SplmtryId")

	@SplmtryId.deleter
	def SplmtryId(self):
		del self._SplmtryId
		self._SplmtryId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssTp', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=SecurityClassificationType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryId', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
	))