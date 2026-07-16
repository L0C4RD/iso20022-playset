# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat41Choice

class SecurityDate24(base_types._BaseFieldType):

	__slots__ = ["_AvlblDt", "_DvddRnkgDt", "_EarlstPmtDt", "_LastTradgDt", "_PmtDt", "_PrpssDt"]
	@property
	def AvlblDt(self):
		return self._AvlblDt

	@AvlblDt.setter
	def AvlblDt(self, value):
		self._AvlblDt = value if value is not None else base_types.UninitialisedField(self, 'AvlblDt', DateFormat41Choice, False)

	@AvlblDt.deleter
	def AvlblDt(self):
		del self._AvlblDt
		self._AvlblDt = base_types.UninitialisedField(self, 'AvlblDt', DateFormat41Choice, False)

	@property
	def DvddRnkgDt(self):
		return self._DvddRnkgDt

	@DvddRnkgDt.setter
	def DvddRnkgDt(self, value):
		self._DvddRnkgDt = value if value is not None else base_types.UninitialisedField(self, 'DvddRnkgDt', DateFormat41Choice, False)

	@DvddRnkgDt.deleter
	def DvddRnkgDt(self):
		del self._DvddRnkgDt
		self._DvddRnkgDt = base_types.UninitialisedField(self, 'DvddRnkgDt', DateFormat41Choice, False)

	@property
	def EarlstPmtDt(self):
		return self._EarlstPmtDt

	@EarlstPmtDt.setter
	def EarlstPmtDt(self, value):
		self._EarlstPmtDt = value if value is not None else base_types.UninitialisedField(self, 'EarlstPmtDt', DateFormat41Choice, False)

	@EarlstPmtDt.deleter
	def EarlstPmtDt(self):
		del self._EarlstPmtDt
		self._EarlstPmtDt = base_types.UninitialisedField(self, 'EarlstPmtDt', DateFormat41Choice, False)

	@property
	def LastTradgDt(self):
		return self._LastTradgDt

	@LastTradgDt.setter
	def LastTradgDt(self, value):
		self._LastTradgDt = value if value is not None else base_types.UninitialisedField(self, 'LastTradgDt', DateFormat41Choice, False)

	@LastTradgDt.deleter
	def LastTradgDt(self):
		del self._LastTradgDt
		self._LastTradgDt = base_types.UninitialisedField(self, 'LastTradgDt', DateFormat41Choice, False)

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDt', DateFormat41Choice, False)

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = base_types.UninitialisedField(self, 'PmtDt', DateFormat41Choice, False)

	@property
	def PrpssDt(self):
		return self._PrpssDt

	@PrpssDt.setter
	def PrpssDt(self, value):
		self._PrpssDt = value if value is not None else base_types.UninitialisedField(self, 'PrpssDt', DateFormat41Choice, False)

	@PrpssDt.deleter
	def PrpssDt(self):
		del self._PrpssDt
		self._PrpssDt = base_types.UninitialisedField(self, 'PrpssDt', DateFormat41Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlblDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddRnkgDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlstPmtDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTradgDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat41Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrpssDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
	))