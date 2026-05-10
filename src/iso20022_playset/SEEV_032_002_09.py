import base_types
import CorporateActionEventProcessingStatusAdvice002V09

class SEEV_032_002_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnEvtPrcgStsAdvc"]
		@property
		def CorpActnEvtPrcgStsAdvc(self):
			return self._CorpActnEvtPrcgStsAdvc

		@CorpActnEvtPrcgStsAdvc.setter
		def CorpActnEvtPrcgStsAdvc(self, value):
			self._CorpActnEvtPrcgStsAdvc = value if type(value) != auto else self.make_default("CorpActnEvtPrcgStsAdvc")

		@CorpActnEvtPrcgStsAdvc.deleter
		def CorpActnEvtPrcgStsAdvc(self):
			del self._CorpActnEvtPrcgStsAdvc
			self._CorpActnEvtPrcgStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnEvtPrcgStsAdvc', type=CorporateActionEventProcessingStatusAdvice002V09, min=1, max=1, mutex_group=None, array=False),
		))

