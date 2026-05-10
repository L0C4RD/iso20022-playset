from . import base_types
import UndertakingIssuanceAdviceV01

class TSRV_002_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgIssncAdvc"]
		@property
		def UdrtkgIssncAdvc(self):
			return self._UdrtkgIssncAdvc

		@UdrtkgIssncAdvc.setter
		def UdrtkgIssncAdvc(self, value):
			self._UdrtkgIssncAdvc = value if type(value) != auto else self.make_default("UdrtkgIssncAdvc")

		@UdrtkgIssncAdvc.deleter
		def UdrtkgIssncAdvc(self):
			del self._UdrtkgIssncAdvc
			self._UdrtkgIssncAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgIssncAdvc', type=UndertakingIssuanceAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

