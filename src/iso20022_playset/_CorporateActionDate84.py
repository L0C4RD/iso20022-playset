# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat30Choice
from . import DateFormat43Choice
from . import DateFormat57Choice

class CorporateActionDate84(base_types._BaseFieldType):

	__slots__ = ["_EarlstPmtDt", "_FXRateFxgDt", "_PmtDt", "_ValDt"]
	@property
	def EarlstPmtDt(self):
		return self._EarlstPmtDt

	@EarlstPmtDt.setter
	def EarlstPmtDt(self, value):
		self._EarlstPmtDt = value if value is not None else base_types.UninitialisedField(self, 'EarlstPmtDt', DateFormat30Choice, False)

	@EarlstPmtDt.deleter
	def EarlstPmtDt(self):
		del self._EarlstPmtDt
		self._EarlstPmtDt = base_types.UninitialisedField(self, 'EarlstPmtDt', DateFormat30Choice, False)

	@property
	def FXRateFxgDt(self):
		return self._FXRateFxgDt

	@FXRateFxgDt.setter
	def FXRateFxgDt(self, value):
		self._FXRateFxgDt = value if value is not None else base_types.UninitialisedField(self, 'FXRateFxgDt', DateFormat43Choice, False)

	@FXRateFxgDt.deleter
	def FXRateFxgDt(self):
		del self._FXRateFxgDt
		self._FXRateFxgDt = base_types.UninitialisedField(self, 'FXRateFxgDt', DateFormat43Choice, False)

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDt', DateFormat30Choice, False)

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = base_types.UninitialisedField(self, 'PmtDt', DateFormat30Choice, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', DateFormat57Choice, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', DateFormat57Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EarlstPmtDt', type=DateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXRateFxgDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat30Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateFormat57Choice, min=0, max=1, mutex_group=None, array=False),
	))