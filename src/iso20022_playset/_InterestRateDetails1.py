# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate
from . import InstalmentPeriod1Code
from . import InterestRate1Code
from . import Max35Text

class InterestRateDetails1(base_types._BaseFieldType):

	__slots__ = ["_OthrTp", "_Prd", "_Rate", "_Tp"]
	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', InstalmentPeriod1Code, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', InstalmentPeriod1Code, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', BaseOneRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', BaseOneRate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', InterestRate1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', InterestRate1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=InstalmentPeriod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=InterestRate1Code, min=0, max=1, mutex_group=None, array=False),
	))