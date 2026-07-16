# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max5NumericText
from . import YesNoIndicator

class Pagination1(base_types._BaseFieldType):

	__slots__ = ["_LastPgInd", "_PgNb"]
	@property
	def LastPgInd(self):
		return self._LastPgInd

	@LastPgInd.setter
	def LastPgInd(self, value):
		self._LastPgInd = value if value is not None else base_types.UninitialisedField(self, 'LastPgInd', YesNoIndicator, False)

	@LastPgInd.deleter
	def LastPgInd(self):
		del self._LastPgInd
		self._LastPgInd = base_types.UninitialisedField(self, 'LastPgInd', YesNoIndicator, False)

	@property
	def PgNb(self):
		return self._PgNb

	@PgNb.setter
	def PgNb(self, value):
		self._PgNb = value if value is not None else base_types.UninitialisedField(self, 'PgNb', Max5NumericText, False)

	@PgNb.deleter
	def PgNb(self):
		del self._PgNb
		self._PgNb = base_types.UninitialisedField(self, 'PgNb', Max5NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LastPgInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PgNb', type=Max5NumericText, min=1, max=1, mutex_group=None, array=False),
	))