from . import base_types
from .NotReported1Code import NotReported1Code
from .OrganisationIdentification15Choice import OrganisationIdentification15Choice

class TradePartyIdentificationQuery11Choice(base_types._BaseFieldType):

	__slots__ = ["_NotRptd", "_Id"]
	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if type(value) != auto else self.make_default("NotRptd")

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=OrganisationIdentification15Choice, min=1, max=None, mutex_group=1, array=True),
	))

