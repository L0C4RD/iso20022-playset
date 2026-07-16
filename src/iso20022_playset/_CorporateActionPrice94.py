# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceFormat62Choice
from . import PriceFormat88Choice

class CorporateActionPrice94(base_types._BaseFieldType):

	__slots__ = ["_CshInLieuOfShrPric", "_MaxCshToInst", "_MinCshToInst", "_MinMltplCshToInst", "_OverSbcptDpstPric"]
	@property
	def CshInLieuOfShrPric(self):
		return self._CshInLieuOfShrPric

	@CshInLieuOfShrPric.setter
	def CshInLieuOfShrPric(self, value):
		self._CshInLieuOfShrPric = value if value is not None else base_types.UninitialisedField(self, 'CshInLieuOfShrPric', PriceFormat88Choice, False)

	@CshInLieuOfShrPric.deleter
	def CshInLieuOfShrPric(self):
		del self._CshInLieuOfShrPric
		self._CshInLieuOfShrPric = base_types.UninitialisedField(self, 'CshInLieuOfShrPric', PriceFormat88Choice, False)

	@property
	def MaxCshToInst(self):
		return self._MaxCshToInst

	@MaxCshToInst.setter
	def MaxCshToInst(self, value):
		self._MaxCshToInst = value if value is not None else base_types.UninitialisedField(self, 'MaxCshToInst', PriceFormat62Choice, False)

	@MaxCshToInst.deleter
	def MaxCshToInst(self):
		del self._MaxCshToInst
		self._MaxCshToInst = base_types.UninitialisedField(self, 'MaxCshToInst', PriceFormat62Choice, False)

	@property
	def MinCshToInst(self):
		return self._MinCshToInst

	@MinCshToInst.setter
	def MinCshToInst(self, value):
		self._MinCshToInst = value if value is not None else base_types.UninitialisedField(self, 'MinCshToInst', PriceFormat62Choice, False)

	@MinCshToInst.deleter
	def MinCshToInst(self):
		del self._MinCshToInst
		self._MinCshToInst = base_types.UninitialisedField(self, 'MinCshToInst', PriceFormat62Choice, False)

	@property
	def MinMltplCshToInst(self):
		return self._MinMltplCshToInst

	@MinMltplCshToInst.setter
	def MinMltplCshToInst(self, value):
		self._MinMltplCshToInst = value if value is not None else base_types.UninitialisedField(self, 'MinMltplCshToInst', PriceFormat62Choice, False)

	@MinMltplCshToInst.deleter
	def MinMltplCshToInst(self):
		del self._MinMltplCshToInst
		self._MinMltplCshToInst = base_types.UninitialisedField(self, 'MinMltplCshToInst', PriceFormat62Choice, False)

	@property
	def OverSbcptDpstPric(self):
		return self._OverSbcptDpstPric

	@OverSbcptDpstPric.setter
	def OverSbcptDpstPric(self, value):
		self._OverSbcptDpstPric = value if value is not None else base_types.UninitialisedField(self, 'OverSbcptDpstPric', PriceFormat88Choice, False)

	@OverSbcptDpstPric.deleter
	def OverSbcptDpstPric(self):
		del self._OverSbcptDpstPric
		self._OverSbcptDpstPric = base_types.UninitialisedField(self, 'OverSbcptDpstPric', PriceFormat88Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInLieuOfShrPric', type=PriceFormat88Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxCshToInst', type=PriceFormat62Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinCshToInst', type=PriceFormat62Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplCshToInst', type=PriceFormat62Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverSbcptDpstPric', type=PriceFormat88Choice, min=0, max=1, mutex_group=None, array=False),
	))