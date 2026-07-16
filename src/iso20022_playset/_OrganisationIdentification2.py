# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BEIIdentifier
from . import BICIdentifier
from . import CHIPSUniversalIdentifier
from . import DunsIdentifier
from . import EANGLNIdentifier
from . import GenericIdentification3
from . import IBEIIdentifier
from . import Max35Text

class OrganisationIdentification2(base_types._BaseFieldType):

	__slots__ = ["_BEI", "_BIC", "_BkPtyId", "_DUNS", "_EANGLN", "_IBEI", "_PrtryId", "_TaxIdNb", "_USCHU"]
	@property
	def BEI(self):
		return self._BEI

	@BEI.setter
	def BEI(self, value):
		self._BEI = value if value is not None else base_types.UninitialisedField(self, 'BEI', BEIIdentifier, False)

	@BEI.deleter
	def BEI(self):
		del self._BEI
		self._BEI = base_types.UninitialisedField(self, 'BEI', BEIIdentifier, False)

	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if value is not None else base_types.UninitialisedField(self, 'BIC', BICIdentifier, False)

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = base_types.UninitialisedField(self, 'BIC', BICIdentifier, False)

	@property
	def BkPtyId(self):
		return self._BkPtyId

	@BkPtyId.setter
	def BkPtyId(self, value):
		self._BkPtyId = value if value is not None else base_types.UninitialisedField(self, 'BkPtyId', Max35Text, False)

	@BkPtyId.deleter
	def BkPtyId(self):
		del self._BkPtyId
		self._BkPtyId = base_types.UninitialisedField(self, 'BkPtyId', Max35Text, False)

	@property
	def DUNS(self):
		return self._DUNS

	@DUNS.setter
	def DUNS(self, value):
		self._DUNS = value if value is not None else base_types.UninitialisedField(self, 'DUNS', DunsIdentifier, False)

	@DUNS.deleter
	def DUNS(self):
		del self._DUNS
		self._DUNS = base_types.UninitialisedField(self, 'DUNS', DunsIdentifier, False)

	@property
	def EANGLN(self):
		return self._EANGLN

	@EANGLN.setter
	def EANGLN(self, value):
		self._EANGLN = value if value is not None else base_types.UninitialisedField(self, 'EANGLN', EANGLNIdentifier, False)

	@EANGLN.deleter
	def EANGLN(self):
		del self._EANGLN
		self._EANGLN = base_types.UninitialisedField(self, 'EANGLN', EANGLNIdentifier, False)

	@property
	def IBEI(self):
		return self._IBEI

	@IBEI.setter
	def IBEI(self, value):
		self._IBEI = value if value is not None else base_types.UninitialisedField(self, 'IBEI', IBEIIdentifier, False)

	@IBEI.deleter
	def IBEI(self):
		del self._IBEI
		self._IBEI = base_types.UninitialisedField(self, 'IBEI', IBEIIdentifier, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', GenericIdentification3, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', GenericIdentification3, False)

	@property
	def TaxIdNb(self):
		return self._TaxIdNb

	@TaxIdNb.setter
	def TaxIdNb(self, value):
		self._TaxIdNb = value if value is not None else base_types.UninitialisedField(self, 'TaxIdNb', Max35Text, False)

	@TaxIdNb.deleter
	def TaxIdNb(self):
		del self._TaxIdNb
		self._TaxIdNb = base_types.UninitialisedField(self, 'TaxIdNb', Max35Text, False)

	@property
	def USCHU(self):
		return self._USCHU

	@USCHU.setter
	def USCHU(self, value):
		self._USCHU = value if value is not None else base_types.UninitialisedField(self, 'USCHU', CHIPSUniversalIdentifier, False)

	@USCHU.deleter
	def USCHU(self):
		del self._USCHU
		self._USCHU = base_types.UninitialisedField(self, 'USCHU', CHIPSUniversalIdentifier, False)

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