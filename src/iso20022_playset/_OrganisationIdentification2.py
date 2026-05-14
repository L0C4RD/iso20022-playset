# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BEIIdentifier import BEIIdentifier
from ._BICIdentifier import BICIdentifier
from ._CHIPSUniversalIdentifier import CHIPSUniversalIdentifier
from ._DunsIdentifier import DunsIdentifier
from ._EANGLNIdentifier import EANGLNIdentifier
from ._GenericIdentification3 import GenericIdentification3
from ._IBEIIdentifier import IBEIIdentifier
from ._Max35Text import Max35Text

class OrganisationIdentification2(base_types._BaseFieldType):

	__slots__ = ["_BEI", "_BIC", "_BkPtyId", "_DUNS", "_EANGLN", "_IBEI", "_PrtryId", "_TaxIdNb", "_USCHU"]
	@property
	def BEI(self):
		return self._BEI

	@BEI.setter
	def BEI(self, value):
		self._BEI = value if type(value) != base_types.auto else self.make_default("BEI")

	@BEI.deleter
	def BEI(self):
		del self._BEI
		self._BEI = None

	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if type(value) != base_types.auto else self.make_default("BIC")

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = None

	@property
	def BkPtyId(self):
		return self._BkPtyId

	@BkPtyId.setter
	def BkPtyId(self, value):
		self._BkPtyId = value if type(value) != base_types.auto else self.make_default("BkPtyId")

	@BkPtyId.deleter
	def BkPtyId(self):
		del self._BkPtyId
		self._BkPtyId = None

	@property
	def DUNS(self):
		return self._DUNS

	@DUNS.setter
	def DUNS(self, value):
		self._DUNS = value if type(value) != base_types.auto else self.make_default("DUNS")

	@DUNS.deleter
	def DUNS(self):
		del self._DUNS
		self._DUNS = None

	@property
	def EANGLN(self):
		return self._EANGLN

	@EANGLN.setter
	def EANGLN(self, value):
		self._EANGLN = value if type(value) != base_types.auto else self.make_default("EANGLN")

	@EANGLN.deleter
	def EANGLN(self):
		del self._EANGLN
		self._EANGLN = None

	@property
	def IBEI(self):
		return self._IBEI

	@IBEI.setter
	def IBEI(self, value):
		self._IBEI = value if type(value) != base_types.auto else self.make_default("IBEI")

	@IBEI.deleter
	def IBEI(self):
		del self._IBEI
		self._IBEI = None

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != base_types.auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	@property
	def TaxIdNb(self):
		return self._TaxIdNb

	@TaxIdNb.setter
	def TaxIdNb(self, value):
		self._TaxIdNb = value if type(value) != base_types.auto else self.make_default("TaxIdNb")

	@TaxIdNb.deleter
	def TaxIdNb(self):
		del self._TaxIdNb
		self._TaxIdNb = None

	@property
	def USCHU(self):
		return self._USCHU

	@USCHU.setter
	def USCHU(self, value):
		self._USCHU = value if type(value) != base_types.auto else self.make_default("USCHU")

	@USCHU.deleter
	def USCHU(self):
		del self._USCHU
		self._USCHU = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BEI', type=BEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BIC', type=BICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DUNS', type=DunsIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EANGLN', type=EANGLNIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IBEI', type=IBEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='USCHU', type=CHIPSUniversalIdentifier, min=0, max=1, mutex_group=None, array=False),
	))