# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat41Choice
from . import DateFormat49Choice
from . import DateFormat64Choice

class CorporateActionDate94(base_types._BaseFieldType):

	__slots__ = ["_EarlstPmtDt", "_FXRateFxgDt", "_PmtDt", "_ValDt"]
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
	def FXRateFxgDt(self):
		return self._FXRateFxgDt

	@FXRateFxgDt.setter
	def FXRateFxgDt(self, value):
		self._FXRateFxgDt = value if value is not None else base_types.UninitialisedField(self, 'FXRateFxgDt', DateFormat49Choice, False)

	@FXRateFxgDt.deleter
	def FXRateFxgDt(self):
		del self._FXRateFxgDt
		self._FXRateFxgDt = base_types.UninitialisedField(self, 'FXRateFxgDt', DateFormat49Choice, False)

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
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', DateFormat64Choice, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', DateFormat64Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EarlstPmtDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXRateFxgDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat41Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateFormat64Choice, min=0, max=1, mutex_group=None, array=False),
	))