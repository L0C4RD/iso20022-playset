# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeQueryCriteria10
from . import TradeRecurrentQuery5

class TradeReportQuery13Choice(base_types._BaseFieldType):

	__slots__ = ["_AdHocQry", "_RcrntQry"]
	@property
	def AdHocQry(self):
		return self._AdHocQry

	@AdHocQry.setter
	def AdHocQry(self, value):
		self._AdHocQry = value if value is not None else base_types.UninitialisedField(self, 'AdHocQry', TradeQueryCriteria10, False)

	@AdHocQry.deleter
	def AdHocQry(self):
		del self._AdHocQry
		self._AdHocQry = base_types.UninitialisedField(self, 'AdHocQry', TradeQueryCriteria10, False)

	@property
	def RcrntQry(self):
		return self._RcrntQry

	@RcrntQry.setter
	def RcrntQry(self, value):
		self._RcrntQry = value if value is not None else base_types.UninitialisedField(self, 'RcrntQry', TradeRecurrentQuery5, False)

	@RcrntQry.deleter
	def RcrntQry(self):
		del self._RcrntQry
		self._RcrntQry = base_types.UninitialisedField(self, 'RcrntQry', TradeRecurrentQuery5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdHocQry', type=TradeQueryCriteria10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcrntQry', type=TradeRecurrentQuery5, min=0, max=1, mutex_group=1, array=False),
	))