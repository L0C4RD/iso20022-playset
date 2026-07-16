# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text

class EndPoint2Choice(base_types._BaseFieldType):

	__slots__ = ["_LastPmtDt", "_NbOfPmts"]
	@property
	def LastPmtDt(self):
		return self._LastPmtDt

	@LastPmtDt.setter
	def LastPmtDt(self, value):
		self._LastPmtDt = value if value is not None else base_types.UninitialisedField(self, 'LastPmtDt', ISODate, False)

	@LastPmtDt.deleter
	def LastPmtDt(self):
		del self._LastPmtDt
		self._LastPmtDt = base_types.UninitialisedField(self, 'LastPmtDt', ISODate, False)

	@property
	def NbOfPmts(self):
		return self._NbOfPmts

	@NbOfPmts.setter
	def NbOfPmts(self, value):
		self._NbOfPmts = value if value is not None else base_types.UninitialisedField(self, 'NbOfPmts', Max35Text, False)

	@NbOfPmts.deleter
	def NbOfPmts(self):
		del self._NbOfPmts
		self._NbOfPmts = base_types.UninitialisedField(self, 'NbOfPmts', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LastPmtDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NbOfPmts', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))