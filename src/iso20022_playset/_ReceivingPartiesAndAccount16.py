# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentificationAndAccount147

class ReceivingPartiesAndAccount16(base_types._BaseFieldType):

	__slots__ = ["_RcvgAgtDtls", "_RcvrsCtdnDtls", "_RcvrsIntrmy1Dtls", "_RcvrsIntrmy2Dtls"]
	@property
	def RcvgAgtDtls(self):
		return self._RcvgAgtDtls

	@RcvgAgtDtls.setter
	def RcvgAgtDtls(self, value):
		self._RcvgAgtDtls = value if value is not None else base_types.UninitialisedField(self, 'RcvgAgtDtls', PartyIdentificationAndAccount147, False)

	@RcvgAgtDtls.deleter
	def RcvgAgtDtls(self):
		del self._RcvgAgtDtls
		self._RcvgAgtDtls = base_types.UninitialisedField(self, 'RcvgAgtDtls', PartyIdentificationAndAccount147, False)

	@property
	def RcvrsCtdnDtls(self):
		return self._RcvrsCtdnDtls

	@RcvrsCtdnDtls.setter
	def RcvrsCtdnDtls(self, value):
		self._RcvrsCtdnDtls = value if value is not None else base_types.UninitialisedField(self, 'RcvrsCtdnDtls', PartyIdentificationAndAccount147, False)

	@RcvrsCtdnDtls.deleter
	def RcvrsCtdnDtls(self):
		del self._RcvrsCtdnDtls
		self._RcvrsCtdnDtls = base_types.UninitialisedField(self, 'RcvrsCtdnDtls', PartyIdentificationAndAccount147, False)

	@property
	def RcvrsIntrmy1Dtls(self):
		return self._RcvrsIntrmy1Dtls

	@RcvrsIntrmy1Dtls.setter
	def RcvrsIntrmy1Dtls(self, value):
		self._RcvrsIntrmy1Dtls = value if value is not None else base_types.UninitialisedField(self, 'RcvrsIntrmy1Dtls', PartyIdentificationAndAccount147, False)

	@RcvrsIntrmy1Dtls.deleter
	def RcvrsIntrmy1Dtls(self):
		del self._RcvrsIntrmy1Dtls
		self._RcvrsIntrmy1Dtls = base_types.UninitialisedField(self, 'RcvrsIntrmy1Dtls', PartyIdentificationAndAccount147, False)

	@property
	def RcvrsIntrmy2Dtls(self):
		return self._RcvrsIntrmy2Dtls

	@RcvrsIntrmy2Dtls.setter
	def RcvrsIntrmy2Dtls(self, value):
		self._RcvrsIntrmy2Dtls = value if value is not None else base_types.UninitialisedField(self, 'RcvrsIntrmy2Dtls', PartyIdentificationAndAccount147, False)

	@RcvrsIntrmy2Dtls.deleter
	def RcvrsIntrmy2Dtls(self):
		del self._RcvrsIntrmy2Dtls
		self._RcvrsIntrmy2Dtls = base_types.UninitialisedField(self, 'RcvrsIntrmy2Dtls', PartyIdentificationAndAccount147, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcvgAgtDtls', type=PartyIdentificationAndAccount147, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrsCtdnDtls', type=PartyIdentificationAndAccount147, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrsIntrmy1Dtls', type=PartyIdentificationAndAccount147, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrsIntrmy2Dtls', type=PartyIdentificationAndAccount147, min=0, max=1, mutex_group=None, array=False),
	))