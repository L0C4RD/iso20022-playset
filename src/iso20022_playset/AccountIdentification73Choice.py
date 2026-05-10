from . import base_types
import AccountIdentification69
import AccountIdentification10

class AccountIdentification73Choice(base_types._BaseFieldType):

	__slots__ = ["_ForAllAccts", "_AcctsList"]
	@property
	def ForAllAccts(self):
		return self._ForAllAccts

	@ForAllAccts.setter
	def ForAllAccts(self, value):
		self._ForAllAccts = value if type(value) != auto else self.make_default("ForAllAccts")

	@ForAllAccts.deleter
	def ForAllAccts(self):
		del self._ForAllAccts
		self._ForAllAccts = None

	@property
	def AcctsList(self):
		return self._AcctsList

	@AcctsList.setter
	def AcctsList(self, value):
		self._AcctsList = value if type(value) != auto else self.make_default("AcctsList")

	@AcctsList.deleter
	def AcctsList(self):
		del self._AcctsList
		self._AcctsList = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ForAllAccts', type=AccountIdentification10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AcctsList', type=AccountIdentification69, min=1, max=None, mutex_group=1, array=True),
	))

