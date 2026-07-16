# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentificationAndAccount147

class DeliveringPartiesAndAccount16(base_types._BaseFieldType):

	__slots__ = ["_DlvrgAgtDtls", "_DlvrrsCtdnDtls", "_DlvrrsIntrmy1Dtls", "_DlvrrsIntrmy2Dtls"]
	@property
	def DlvrgAgtDtls(self):
		return self._DlvrgAgtDtls

	@DlvrgAgtDtls.setter
	def DlvrgAgtDtls(self, value):
		self._DlvrgAgtDtls = value if value is not None else base_types.UninitialisedField(self, 'DlvrgAgtDtls', PartyIdentificationAndAccount147, False)

	@DlvrgAgtDtls.deleter
	def DlvrgAgtDtls(self):
		del self._DlvrgAgtDtls
		self._DlvrgAgtDtls = base_types.UninitialisedField(self, 'DlvrgAgtDtls', PartyIdentificationAndAccount147, False)

	@property
	def DlvrrsCtdnDtls(self):
		return self._DlvrrsCtdnDtls

	@DlvrrsCtdnDtls.setter
	def DlvrrsCtdnDtls(self, value):
		self._DlvrrsCtdnDtls = value if value is not None else base_types.UninitialisedField(self, 'DlvrrsCtdnDtls', PartyIdentificationAndAccount147, False)

	@DlvrrsCtdnDtls.deleter
	def DlvrrsCtdnDtls(self):
		del self._DlvrrsCtdnDtls
		self._DlvrrsCtdnDtls = base_types.UninitialisedField(self, 'DlvrrsCtdnDtls', PartyIdentificationAndAccount147, False)

	@property
	def DlvrrsIntrmy1Dtls(self):
		return self._DlvrrsIntrmy1Dtls

	@DlvrrsIntrmy1Dtls.setter
	def DlvrrsIntrmy1Dtls(self, value):
		self._DlvrrsIntrmy1Dtls = value if value is not None else base_types.UninitialisedField(self, 'DlvrrsIntrmy1Dtls', PartyIdentificationAndAccount147, False)

	@DlvrrsIntrmy1Dtls.deleter
	def DlvrrsIntrmy1Dtls(self):
		del self._DlvrrsIntrmy1Dtls
		self._DlvrrsIntrmy1Dtls = base_types.UninitialisedField(self, 'DlvrrsIntrmy1Dtls', PartyIdentificationAndAccount147, False)

	@property
	def DlvrrsIntrmy2Dtls(self):
		return self._DlvrrsIntrmy2Dtls

	@DlvrrsIntrmy2Dtls.setter
	def DlvrrsIntrmy2Dtls(self, value):
		self._DlvrrsIntrmy2Dtls = value if value is not None else base_types.UninitialisedField(self, 'DlvrrsIntrmy2Dtls', PartyIdentificationAndAccount147, False)

	@DlvrrsIntrmy2Dtls.deleter
	def DlvrrsIntrmy2Dtls(self):
		del self._DlvrrsIntrmy2Dtls
		self._DlvrrsIntrmy2Dtls = base_types.UninitialisedField(self, 'DlvrrsIntrmy2Dtls', PartyIdentificationAndAccount147, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgAgtDtls', type=PartyIdentificationAndAccount147, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrrsCtdnDtls', type=PartyIdentificationAndAccount147, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrrsIntrmy1Dtls', type=PartyIdentificationAndAccount147, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrrsIntrmy2Dtls', type=PartyIdentificationAndAccount147, min=0, max=1, mutex_group=None, array=False),
	))