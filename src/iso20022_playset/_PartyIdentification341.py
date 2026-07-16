# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max256Text
from . import Max35Text
from . import PartyIdentification198Choice
from . import PersonName2

class PartyIdentification341(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_CpnyRegrShrhldrId", "_CtryOfIncorprtn", "_EmailAdr", "_Id", "_NmAndAdr"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def CpnyRegrShrhldrId(self):
		return self._CpnyRegrShrhldrId

	@CpnyRegrShrhldrId.setter
	def CpnyRegrShrhldrId(self, value):
		self._CpnyRegrShrhldrId = value if value is not None else base_types.UninitialisedField(self, 'CpnyRegrShrhldrId', Max35Text, False)

	@CpnyRegrShrhldrId.deleter
	def CpnyRegrShrhldrId(self):
		del self._CpnyRegrShrhldrId
		self._CpnyRegrShrhldrId = base_types.UninitialisedField(self, 'CpnyRegrShrhldrId', Max35Text, False)

	@property
	def CtryOfIncorprtn(self):
		return self._CtryOfIncorprtn

	@CtryOfIncorprtn.setter
	def CtryOfIncorprtn(self, value):
		self._CtryOfIncorprtn = value if value is not None else base_types.UninitialisedField(self, 'CtryOfIncorprtn', CountryCode, False)

	@CtryOfIncorprtn.deleter
	def CtryOfIncorprtn(self):
		del self._CtryOfIncorprtn
		self._CtryOfIncorprtn = base_types.UninitialisedField(self, 'CtryOfIncorprtn', CountryCode, False)

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if value is not None else base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification198Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification198Choice, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', PersonName2, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', PersonName2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyRegrShrhldrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncorprtn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification198Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=PersonName2, min=1, max=1, mutex_group=None, array=False),
	))