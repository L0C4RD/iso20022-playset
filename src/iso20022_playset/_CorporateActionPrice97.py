# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PriceFormat62Choice import PriceFormat62Choice
from ._PriceFormat92Choice import PriceFormat92Choice
from ._PriceFormat93Choice import PriceFormat93Choice

class CorporateActionPrice97(base_types._BaseFieldType):

	__slots__ = ["_CshInLieuOfShrPric", "_FrstBidIncrmtPric", "_LastBidIncrmtPric", "_MaxCshToInst", "_MaxPric", "_MinCshToInst", "_MinMltplCshToInst", "_MinPric", "_OverSbcptDpstPric"]
	@property
	def CshInLieuOfShrPric(self):
		return self._CshInLieuOfShrPric

	@CshInLieuOfShrPric.setter
	def CshInLieuOfShrPric(self, value):
		self._CshInLieuOfShrPric = value if type(value) != base_types.auto else self.make_default("CshInLieuOfShrPric")

	@CshInLieuOfShrPric.deleter
	def CshInLieuOfShrPric(self):
		del self._CshInLieuOfShrPric
		self._CshInLieuOfShrPric = None

	@property
	def FrstBidIncrmtPric(self):
		return self._FrstBidIncrmtPric

	@FrstBidIncrmtPric.setter
	def FrstBidIncrmtPric(self, value):
		self._FrstBidIncrmtPric = value if type(value) != base_types.auto else self.make_default("FrstBidIncrmtPric")

	@FrstBidIncrmtPric.deleter
	def FrstBidIncrmtPric(self):
		del self._FrstBidIncrmtPric
		self._FrstBidIncrmtPric = None

	@property
	def LastBidIncrmtPric(self):
		return self._LastBidIncrmtPric

	@LastBidIncrmtPric.setter
	def LastBidIncrmtPric(self, value):
		self._LastBidIncrmtPric = value if type(value) != base_types.auto else self.make_default("LastBidIncrmtPric")

	@LastBidIncrmtPric.deleter
	def LastBidIncrmtPric(self):
		del self._LastBidIncrmtPric
		self._LastBidIncrmtPric = None

	@property
	def MaxCshToInst(self):
		return self._MaxCshToInst

	@MaxCshToInst.setter
	def MaxCshToInst(self, value):
		self._MaxCshToInst = value if type(value) != base_types.auto else self.make_default("MaxCshToInst")

	@MaxCshToInst.deleter
	def MaxCshToInst(self):
		del self._MaxCshToInst
		self._MaxCshToInst = None

	@property
	def MaxPric(self):
		return self._MaxPric

	@MaxPric.setter
	def MaxPric(self, value):
		self._MaxPric = value if type(value) != base_types.auto else self.make_default("MaxPric")

	@MaxPric.deleter
	def MaxPric(self):
		del self._MaxPric
		self._MaxPric = None

	@property
	def MinCshToInst(self):
		return self._MinCshToInst

	@MinCshToInst.setter
	def MinCshToInst(self, value):
		self._MinCshToInst = value if type(value) != base_types.auto else self.make_default("MinCshToInst")

	@MinCshToInst.deleter
	def MinCshToInst(self):
		del self._MinCshToInst
		self._MinCshToInst = None

	@property
	def MinMltplCshToInst(self):
		return self._MinMltplCshToInst

	@MinMltplCshToInst.setter
	def MinMltplCshToInst(self, value):
		self._MinMltplCshToInst = value if type(value) != base_types.auto else self.make_default("MinMltplCshToInst")

	@MinMltplCshToInst.deleter
	def MinMltplCshToInst(self):
		del self._MinMltplCshToInst
		self._MinMltplCshToInst = None

	@property
	def MinPric(self):
		return self._MinPric

	@MinPric.setter
	def MinPric(self, value):
		self._MinPric = value if type(value) != base_types.auto else self.make_default("MinPric")

	@MinPric.deleter
	def MinPric(self):
		del self._MinPric
		self._MinPric = None

	@property
	def OverSbcptDpstPric(self):
		return self._OverSbcptDpstPric

	@OverSbcptDpstPric.setter
	def OverSbcptDpstPric(self, value):
		self._OverSbcptDpstPric = value if type(value) != base_types.auto else self.make_default("OverSbcptDpstPric")

	@OverSbcptDpstPric.deleter
	def OverSbcptDpstPric(self):
		del self._OverSbcptDpstPric
		self._OverSbcptDpstPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat92Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstBidIncrmtPric', type=PriceFormat93Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastBidIncrmtPric', type=PriceFormat93Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxCshToInst', type=PriceFormat62Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxPric', type=PriceFormat93Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinCshToInst', type=PriceFormat62Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplCshToInst', type=PriceFormat62Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPric', type=PriceFormat93Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverSbcptDpstPric', type=PriceFormat92Choice, min=0, max=1, mutex_group=None, array=False),
	))