# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text
from ._Max3NumericText import Max3NumericText
from ._Max70Text import Max70Text

class LodgingRoom2(base_types._BaseFieldType):

	__slots__ = ["_Adlts", "_BedTp", "_Chldrn", "_DalyRate", "_Gsts", "_Lctn", "_Tp"]
	@property
	def Adlts(self):
		return self._Adlts

	@Adlts.setter
	def Adlts(self, value):
		self._Adlts = value if type(value) != base_types.auto else self.make_default("Adlts")

	@Adlts.deleter
	def Adlts(self):
		del self._Adlts
		self._Adlts = None

	@property
	def BedTp(self):
		return self._BedTp

	@BedTp.setter
	def BedTp(self, value):
		self._BedTp = value if type(value) != base_types.auto else self.make_default("BedTp")

	@BedTp.deleter
	def BedTp(self):
		del self._BedTp
		self._BedTp = None

	@property
	def Chldrn(self):
		return self._Chldrn

	@Chldrn.setter
	def Chldrn(self, value):
		self._Chldrn = value if type(value) != base_types.auto else self.make_default("Chldrn")

	@Chldrn.deleter
	def Chldrn(self):
		del self._Chldrn
		self._Chldrn = None

	@property
	def DalyRate(self):
		return self._DalyRate

	@DalyRate.setter
	def DalyRate(self, value):
		self._DalyRate = value if type(value) != base_types.auto else self.make_default("DalyRate")

	@DalyRate.deleter
	def DalyRate(self):
		del self._DalyRate
		self._DalyRate = None

	@property
	def Gsts(self):
		return self._Gsts

	@Gsts.setter
	def Gsts(self, value):
		self._Gsts = value if type(value) != base_types.auto else self.make_default("Gsts")

	@Gsts.deleter
	def Gsts(self):
		del self._Gsts
		self._Gsts = None

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != base_types.auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adlts', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BedTp', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chldrn', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DalyRate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Gsts', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))