# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotReported1Code
from . import PartyIdentification248Choice

class TradePartyIdentificationQuery10Choice(base_types._BaseFieldType):

	__slots__ = ["_Id", "_NotRptd"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification248Choice, True)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification248Choice, True)

	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if value is not None else base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification248Choice, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=1, array=False),
	))