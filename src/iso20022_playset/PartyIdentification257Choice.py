from . import base_types
import DTI2024Identifier
import NameAndAddress5
import CountryCode
import AnyBICDec2014Identifier

class PartyIdentification257Choice(base_types._BaseFieldType):

	__slots__ = ["_NmAndAdr", "_AnyBIC", "_DgtlLdgrId", "_Ctry"]
	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if type(value) != auto else self.make_default("AnyBIC")

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = None

	@property
	def DgtlLdgrId(self):
		return self._DgtlLdgrId

	@DgtlLdgrId.setter
	def DgtlLdgrId(self, value):
		self._DgtlLdgrId = value if type(value) != auto else self.make_default("DgtlLdgrId")

	@DgtlLdgrId.deleter
	def DgtlLdgrId(self):
		del self._DgtlLdgrId
		self._DgtlLdgrId = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DgtlLdgrId', type=DTI2024Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
	))

