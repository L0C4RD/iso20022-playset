import base_types
import PostalAddress1
import Party2Choice
import CountryCode
import Max70Text

class PartyIdentification8(base_types._BaseFieldType):

	__slots__ = ["_PstlAdr", "_Id", "_CtryOfRes", "_Nm"]
	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

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

	@property
	def CtryOfRes(self):
		return self._CtryOfRes

	@CtryOfRes.setter
	def CtryOfRes(self, value):
		self._CtryOfRes = value if type(value) != auto else self.make_default("CtryOfRes")

	@CtryOfRes.deleter
	def CtryOfRes(self):
		del self._CtryOfRes
		self._CtryOfRes = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Party2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfRes', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

