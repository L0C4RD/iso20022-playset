# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PriceFormat61Choice import PriceFormat61Choice
from ._PriceFormat74Choice import PriceFormat74Choice

class CorporateActionPrice86(base_types._BaseFieldType):

	__slots__ = ["_CshInLieuOfShrPric", "_MaxCshToInst", "_MinCshToInst", "_MinMltplCshToInst", "_OverSbcptDpstPric"]
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
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat74Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxCshToInst', type=PriceFormat61Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinCshToInst', type=PriceFormat61Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplCshToInst', type=PriceFormat61Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverSbcptDpstPric', type=PriceFormat74Choice, min=0, max=1, mutex_group=None, array=False),
	))