# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount17
from . import Number

class SettlementCategoryTotal2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Cnt", "_IntrchngFee", "_PrcgFee"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', Amount17, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', Amount17, False)

	@property
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if value is not None else base_types.UninitialisedField(self, 'Cnt', Number, False)

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = base_types.UninitialisedField(self, 'Cnt', Number, False)

	@property
	def IntrchngFee(self):
		return self._IntrchngFee

	@IntrchngFee.setter
	def IntrchngFee(self, value):
		self._IntrchngFee = value if value is not None else base_types.UninitialisedField(self, 'IntrchngFee', Amount17, False)

	@IntrchngFee.deleter
	def IntrchngFee(self):
		del self._IntrchngFee
		self._IntrchngFee = base_types.UninitialisedField(self, 'IntrchngFee', Amount17, False)

	@property
	def PrcgFee(self):
		return self._PrcgFee

	@PrcgFee.setter
	def PrcgFee(self, value):
		self._PrcgFee = value if value is not None else base_types.UninitialisedField(self, 'PrcgFee', Amount17, False)

	@PrcgFee.deleter
	def PrcgFee(self):
		del self._PrcgFee
		self._PrcgFee = base_types.UninitialisedField(self, 'PrcgFee', Amount17, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=Amount17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFee', type=Amount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgFee', type=Amount17, min=0, max=1, mutex_group=None, array=False),
	))