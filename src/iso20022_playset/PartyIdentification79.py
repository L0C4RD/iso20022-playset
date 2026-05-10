import base_types
import PartyIdentification76
import PersonOrOrganisation2Choice

class PartyIdentification79(base_types._BaseFieldType):

	__slots__ = ["_DcsnMakr", "_AcctOwnr"]
	@property
	def DcsnMakr(self):
		return self._DcsnMakr

	@DcsnMakr.setter
	def DcsnMakr(self, value):
		self._DcsnMakr = value if type(value) != auto else self.make_default("DcsnMakr")

	@DcsnMakr.deleter
	def DcsnMakr(self):
		del self._DcsnMakr
		self._DcsnMakr = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DcsnMakr', type=PersonOrOrganisation2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification76, min=1, max=None, mutex_group=None, array=True),
	))

