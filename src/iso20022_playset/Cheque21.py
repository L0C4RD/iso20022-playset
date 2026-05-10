import base_types
import Max35Text
import FinancialInstitutionIdentification15
import PartyIdentification139

class Cheque21(base_types._BaseFieldType):

	__slots__ = ["_DrweeId", "_Nb", "_PyeeId", "_DrwrId"]
	@property
	def DrweeId(self):
		return self._DrweeId

	@DrweeId.setter
	def DrweeId(self, value):
		self._DrweeId = value if type(value) != auto else self.make_default("DrweeId")

	@DrweeId.deleter
	def DrweeId(self):
		del self._DrweeId
		self._DrweeId = None

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def PyeeId(self):
		return self._PyeeId

	@PyeeId.setter
	def PyeeId(self, value):
		self._PyeeId = value if type(value) != auto else self.make_default("PyeeId")

	@PyeeId.deleter
	def PyeeId(self):
		del self._PyeeId
		self._PyeeId = None

	@property
	def DrwrId(self):
		return self._DrwrId

	@DrwrId.setter
	def DrwrId(self, value):
		self._DrwrId = value if type(value) != auto else self.make_default("DrwrId")

	@DrwrId.deleter
	def DrwrId(self):
		del self._DrwrId
		self._DrwrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DrweeId', type=FinancialInstitutionIdentification15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyeeId', type=PartyIdentification139, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwrId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
	))

