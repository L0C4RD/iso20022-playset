from . import base_types
from .PaymentStatusTrackerUpdateV04 import PaymentStatusTrackerUpdateV04

class TRCK_001_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PmtStsTrckrUpd"]
		@property
		def PmtStsTrckrUpd(self):
			return self._PmtStsTrckrUpd

		@PmtStsTrckrUpd.setter
		def PmtStsTrckrUpd(self, value):
			self._PmtStsTrckrUpd = value if type(value) != base_types.auto else self.make_default("PmtStsTrckrUpd")

		@PmtStsTrckrUpd.deleter
		def PmtStsTrckrUpd(self):
			del self._PmtStsTrckrUpd
			self._PmtStsTrckrUpd = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtStsTrckrUpd', type=PaymentStatusTrackerUpdateV04, min=1, max=1, mutex_group=None, array=False),
		))

