import base_types
import GenericIdentification80
import PledgeeTypeAndAnyBICIdentifier2
import PledgeeTypeAndText1

class PledgeeFormat5Choice(base_types._BaseFieldType):

	__slots__ = ["_TpAndId", "_Prtry", "_Id"]
	@property
	def TpAndId(self):
		return self._TpAndId

	@TpAndId.setter
	def TpAndId(self, value):
		self._TpAndId = value if type(value) != auto else self.make_default("TpAndId")

	@TpAndId.deleter
	def TpAndId(self):
		del self._TpAndId
		self._TpAndId = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

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
		base_types.FieldEntry(name='TpAndId', type=PledgeeTypeAndAnyBICIdentifier2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification80, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=PledgeeTypeAndText1, min=0, max=1, mutex_group=1, array=False),
	))

