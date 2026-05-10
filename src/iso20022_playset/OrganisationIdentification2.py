import base_types
import CHIPSUniversalIdentifier
import IBEIIdentifier
import DunsIdentifier
import BICIdentifier
import BEIIdentifier
import GenericIdentification3
import Max35Text
import EANGLNIdentifier

class OrganisationIdentification2(base_types._BaseFieldType):

	__slots__ = ["_BIC", "_PrtryId", "_USCHU", "_BEI", "_TaxIdNb", "_EANGLN", "_DUNS", "_BkPtyId", "_IBEI"]
	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if type(value) != auto else self.make_default("BIC")

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = None

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	@property
	def USCHU(self):
		return self._USCHU

	@USCHU.setter
	def USCHU(self, value):
		self._USCHU = value if type(value) != auto else self.make_default("USCHU")

	@USCHU.deleter
	def USCHU(self):
		del self._USCHU
		self._USCHU = None

	@property
	def BEI(self):
		return self._BEI

	@BEI.setter
	def BEI(self, value):
		self._BEI = value if type(value) != auto else self.make_default("BEI")

	@BEI.deleter
	def BEI(self):
		del self._BEI
		self._BEI = None

	@property
	def TaxIdNb(self):
		return self._TaxIdNb

	@TaxIdNb.setter
	def TaxIdNb(self, value):
		self._TaxIdNb = value if type(value) != auto else self.make_default("TaxIdNb")

	@TaxIdNb.deleter
	def TaxIdNb(self):
		del self._TaxIdNb
		self._TaxIdNb = None

	@property
	def EANGLN(self):
		return self._EANGLN

	@EANGLN.setter
	def EANGLN(self, value):
		self._EANGLN = value if type(value) != auto else self.make_default("EANGLN")

	@EANGLN.deleter
	def EANGLN(self):
		del self._EANGLN
		self._EANGLN = None

	@property
	def DUNS(self):
		return self._DUNS

	@DUNS.setter
	def DUNS(self, value):
		self._DUNS = value if type(value) != auto else self.make_default("DUNS")

	@DUNS.deleter
	def DUNS(self):
		del self._DUNS
		self._DUNS = None

	@property
	def BkPtyId(self):
		return self._BkPtyId

	@BkPtyId.setter
	def BkPtyId(self, value):
		self._BkPtyId = value if type(value) != auto else self.make_default("BkPtyId")

	@BkPtyId.deleter
	def BkPtyId(self):
		del self._BkPtyId
		self._BkPtyId = None

	@property
	def IBEI(self):
		return self._IBEI

	@IBEI.setter
	def IBEI(self, value):
		self._IBEI = value if type(value) != auto else self.make_default("IBEI")

	@IBEI.deleter
	def IBEI(self):
		del self._IBEI
		self._IBEI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BIC', type=BICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='USCHU', type=CHIPSUniversalIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BEI', type=BEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EANGLN', type=EANGLNIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DUNS', type=DunsIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IBEI', type=IBEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

