# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Number

class OptionDateOrPeriod1Choice(base_types._BaseFieldType):

	__slots__ = ["_EarlstExrcDt", "_NtcePrd"]
	@property
	def EarlstExrcDt(self):
		return self._EarlstExrcDt

	@EarlstExrcDt.setter
	def EarlstExrcDt(self, value):
		self._EarlstExrcDt = value if value is not None else base_types.UninitialisedField(self, 'EarlstExrcDt', ISODate, False)

	@EarlstExrcDt.deleter
	def EarlstExrcDt(self):
		del self._EarlstExrcDt
		self._EarlstExrcDt = base_types.UninitialisedField(self, 'EarlstExrcDt', ISODate, False)

	@property
	def NtcePrd(self):
		return self._NtcePrd

	@NtcePrd.setter
	def NtcePrd(self, value):
		self._NtcePrd = value if value is not None else base_types.UninitialisedField(self, 'NtcePrd', Number, False)

	@NtcePrd.deleter
	def NtcePrd(self):
		del self._NtcePrd
		self._NtcePrd = base_types.UninitialisedField(self, 'NtcePrd', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EarlstExrcDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtcePrd', type=Number, min=0, max=1, mutex_group=1, array=False),
	))