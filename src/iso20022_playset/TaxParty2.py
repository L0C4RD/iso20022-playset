import base_types
import Max35Text
import TaxAuthorisation1

class TaxParty2(base_types._BaseFieldType):

	__slots__ = ["_TaxTp", "_RegnId", "_Authstn", "_TaxId"]
	@property
	def TaxTp(self):
		return self._TaxTp

	@TaxTp.setter
	def TaxTp(self, value):
		self._TaxTp = value if type(value) != auto else self.make_default("TaxTp")

	@TaxTp.deleter
	def TaxTp(self):
		del self._TaxTp
		self._TaxTp = None

	@property
	def RegnId(self):
		return self._RegnId

	@RegnId.setter
	def RegnId(self, value):
		self._RegnId = value if type(value) != auto else self.make_default("RegnId")

	@RegnId.deleter
	def RegnId(self):
		del self._RegnId
		self._RegnId = None

	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if type(value) != auto else self.make_default("Authstn")

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = None

	@property
	def TaxId(self):
		return self._TaxId

	@TaxId.setter
	def TaxId(self, value):
		self._TaxId = value if type(value) != auto else self.make_default("TaxId")

	@TaxId.deleter
	def TaxId(self):
		del self._TaxId
		self._TaxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authstn', type=TaxAuthorisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

