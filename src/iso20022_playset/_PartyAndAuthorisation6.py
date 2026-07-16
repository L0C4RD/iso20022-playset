# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Authorisation2
from . import Max15PlusSignedNumericText
from . import Modification1Code
from . import PartyOrGroup3Choice

class PartyAndAuthorisation6(base_types._BaseFieldType):

	__slots__ = ["_Authstn", "_ModCd", "_PtyOrGrp", "_SgntrOrdr"]
	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if value is not None else base_types.UninitialisedField(self, 'Authstn', Authorisation2, False)

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = base_types.UninitialisedField(self, 'Authstn', Authorisation2, False)

	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if value is not None else base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@property
	def PtyOrGrp(self):
		return self._PtyOrGrp

	@PtyOrGrp.setter
	def PtyOrGrp(self, value):
		self._PtyOrGrp = value if value is not None else base_types.UninitialisedField(self, 'PtyOrGrp', PartyOrGroup3Choice, False)

	@PtyOrGrp.deleter
	def PtyOrGrp(self):
		del self._PtyOrGrp
		self._PtyOrGrp = base_types.UninitialisedField(self, 'PtyOrGrp', PartyOrGroup3Choice, False)

	@property
	def SgntrOrdr(self):
		return self._SgntrOrdr

	@SgntrOrdr.setter
	def SgntrOrdr(self, value):
		self._SgntrOrdr = value if value is not None else base_types.UninitialisedField(self, 'SgntrOrdr', Max15PlusSignedNumericText, False)

	@SgntrOrdr.deleter
	def SgntrOrdr(self):
		del self._SgntrOrdr
		self._SgntrOrdr = base_types.UninitialisedField(self, 'SgntrOrdr', Max15PlusSignedNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Authstn', type=Authorisation2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyOrGrp', type=PartyOrGroup3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrOrdr', type=Max15PlusSignedNumericText, min=0, max=1, mutex_group=None, array=False),
	))