import base_types
import PersonName2
import Max35Text
import CountryCode
import Max256Text
import PartyIdentification198Choice

class PartyIdentification269(base_types._BaseFieldType):

	__slots__ = ["_Id", "_CtryOfIncorprtn", "_EmailAdr", "_NmAndAdr", "_CpnyRegrShrhldrId"]
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
	def CtryOfIncorprtn(self):
		return self._CtryOfIncorprtn

	@CtryOfIncorprtn.setter
	def CtryOfIncorprtn(self, value):
		self._CtryOfIncorprtn = value if type(value) != auto else self.make_default("CtryOfIncorprtn")

	@CtryOfIncorprtn.deleter
	def CtryOfIncorprtn(self):
		del self._CtryOfIncorprtn
		self._CtryOfIncorprtn = None

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if type(value) != auto else self.make_default("EmailAdr")

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = None

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
	def CpnyRegrShrhldrId(self):
		return self._CpnyRegrShrhldrId

	@CpnyRegrShrhldrId.setter
	def CpnyRegrShrhldrId(self, value):
		self._CpnyRegrShrhldrId = value if type(value) != auto else self.make_default("CpnyRegrShrhldrId")

	@CpnyRegrShrhldrId.deleter
	def CpnyRegrShrhldrId(self):
		del self._CpnyRegrShrhldrId
		self._CpnyRegrShrhldrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification198Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncorprtn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=PersonName2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyRegrShrhldrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

